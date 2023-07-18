import React, { useState, useEffect } from "react";

const ShowExpense = () => {

    const [groupName, setGroupName] = useState([]);
    const [allGroups, setAllGroups] = useState([]);
    const [debts, setDebts] = useState([]);
    
    useEffect(() => {
        const fetchGroups = async () => {
          
            const response = await fetch("/myApp/creategroup", {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
      
          });
            const data = await response.json();
            setAllGroups(data);
           
        };
      
        fetchGroups();
      }, []);

    const handleSelection = (event) => {
      setGroupName(Array.from(event.target.selectedOptions, option => option.value));
    };

    useEffect(() => {
        const fetchExpense = async () => {
            
            const response = await fetch(`/myApp/getsplit?group=${groupName}`, {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
      
          });
            const data = await response.json();
            setDebts(data);
        
            
           
        };

        
        
        fetchExpense();
        
    }, [groupName]);

    
  
  
    return (
      <div>
        <h1>Balances</h1>
     
          <div>
            <label>Groups:</label>
            <select
              value={groupName}
              onChange={handleSelection}
              required
            >
              {allGroups.map((group, index) => (
                <option key={index} value={group}>{group}</option>
              ))}
            </select>
          </div>
          <div>
          
      {debts.map((debt, index) => (
        <div key={index}>
          <p>{debt[0]} owes {debt[1]} ${debt[2]}</p>

          </div>))}
          </div>
          
          
         
      </div>
    );



    
    
        

    

    
  }

export default ShowExpense;