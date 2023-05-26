import React, { useState, useEffect } from "react";

const CreateGroup = () => {
  const [groupName, setGroupName] = useState("");
  const [debts, setDebts] = useState("");
  const [members, setMembers] = useState([]);


  useEffect(() => {
    const fetchMembers = async () => {
      
        const response = await fetch("/myApp/userprofile", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
  
      });
        const data = await response.json();
        setMembers(data);
       
    };
  
    fetchMembers();
  }, []);


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
          debts,
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
      console.error(error);
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
          <select
            multiple
            value={members}
            onChange={(e) => setMembers(Array.from(e.target.selectedOptions, option => option.value))}
          >
            {members.map((member, index) => (
              <option key={index} value={member}>{member}</option>
            ))}
          </select>
        </div>
        <button type="submit">Create Group</button>
      </form>
    </div>
  );
};

export default CreateGroup;
