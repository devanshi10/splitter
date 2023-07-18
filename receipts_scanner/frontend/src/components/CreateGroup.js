import React, { useState, useEffect } from "react";

const CreateGroup = () => {
  const [groupName, setGroupName] = useState("");
  const [debts, setDebts] = useState("");
  const [members, setMembers] = useState([]);
  const [allMembers, setAllMembers] = useState([]);

  useEffect(() => {
    const fetchMembers = async () => {
      
        const response = await fetch("/myApp/userprofile", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
  
      });
        const data = await response.json();
        setAllMembers(data);
       
    };
  
    fetchMembers();
  }, []);

  const handleCheckboxChange = (event) => {
    const { value, checked } = event.target;

    if (checked) {
      setMembers([...members, value]);
    } else {
      setMembers(members.filter(member => member !== value));
    }
  };
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("/myApp/creategroup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
  
          group_name: groupName,
          members: members,
        }),
      });
     
      if (response.ok) {
        // Group created successfully
        return (<p>Group created</p>);
      } else {
        // Handle error response
        console.error("Error:", response.statusText);
      }
    } catch (error) {
      // Handle network or other errors
      
      console.error("Error:", error);
    }
  };

  return (
    <div>
      <h1>Create Group</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Group Name:</label>
          <input
            type="text"
            value={groupName}
            onChange={(e) => setGroupName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Members:</label>
          {allMembers.map((member, index) => (
        <div key={index}>
          <label>
            <input
              type="checkbox"
              value={member}
              checked={members.includes(member)}
              onChange={handleCheckboxChange}
            />
            {member}
          </label>
        </div>
      ))}
        </div>
        <button type="submit">Create Group</button>
      </form>
    </div>
  );
};

export default CreateGroup;
