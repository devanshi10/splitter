import React, { useState, useEffect } from "react";

const CreateExpense = () => {
  const [expenseName, setExpenseName] = useState("");
  const [paidBy, setPaidBy] = useState([]);
  const [groups, setGroups] = useState([]);
  const [splitbtw, setSplitbtw] = useState([]);
  const [amount, setAmount] = useState(0.0);


  useEffect(() => {
    const fetchGroups = async () => {
      
        const response = await fetch("/myApp/creategroup", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
  
      });
        const data = await response.json();
        setGroups(data);
       
    };
  
    fetchGroups();
  }, []);

  const handleSelection = (event) => {
    setGroups(Array.from(event.target.selectedOptions, option => option.value));
  };

  useEffect(() => {
    const fetchMembers = async () => {
        
        const response = await fetch(`/myApp/creategroup?group=${groups[0]}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
  
      });
        const data = await response.json();
        setPaidBy(data)
        setSplitbtw(data);
        
       
    };
    
    fetchMembers();

  }, [groups]);



  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("/myApp/createexpense", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          expense_name: expenseName,
          selectedGroup: groups[0],
          paidBy: paidBy[0],
          splitbtw,
          amount
        }),
      });
     
      if (response.ok) {
        // Group created successfully
     
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
      <h1>Create Expense</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Expense name:</label>
          <input
            type="text"
            value={expenseName}
            onChange={(e) => setExpenseName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Groups:</label>
          <select
            value={groups}
            onChange={handleSelection}
            required
          >
            {groups.map((group, index) => (
              <option key={index} value={group}>{group}</option>
            ))}
          </select>
        </div>
        <div>
          <label>Paid By:</label>
          <select
            value={paidBy}
            onChange={(e) => setPaidBy(Array.from(e.target.selectedOptions, option => option.value))}
            required
          >
            {paidBy.map((member, index) => (
              <option key={index} value={member}>{member}</option>
            ))}
          </select>
        </div>
        <div>
          <label>Split Between:</label>
          <select
            multiple
            value={splitbtw}
            onChange={(e) => setSplitbtw(Array.from(e.target.selectedOptions, option => option.value))}
            required
          >
            {splitbtw.map((member, index) => (
              <option key={index} value={member}>{member}</option>
            ))}
          </select>
        </div>
        <div>
          <label>Amount:</label>
          <input
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            required
          />
        </div>
        
        <button type="submit">Create Expense</button>
      </form>
    </div>
  );
};

export default CreateExpense;
