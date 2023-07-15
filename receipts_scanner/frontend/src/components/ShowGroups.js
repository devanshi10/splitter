import React, { useState, useEffect } from "react";
import {Link, Router, Routes, Route, useNavigate} from 'react-router-dom';
import CreateExpense from "./CreatExpense";

const ShowGroups = () => {
    const [groupNames, setGroupNames] = useState([]);
    
    useEffect(() => {
        const fetchGroups = async () => {
          
            const response = await fetch("/myApp/creategroup", {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
      
          });
            const data = await response.json();
            setGroupNames(data);
           
        };
      
        fetchGroups();
      }, []);


    const navigate = useNavigate();

    const navigateToPage = () => {
         
        navigate("/createexpense");
       };  

      return (
        
      <div>
      <h4>Group Names:</h4>
   
      {groupNames.map((groupName, index) => (
      
        <button key={index} onClick={navigateToPage}>
          {groupName}
        </button>
      
      
      ))}
    
    </div>
    
 
    );

    
  
      };


export default ShowGroups;
