import React, { Component } from "react";
import CreateUser from "./CreateUser";
import CreateGroup from "./CreateGroup";
import CreateExpense from "./CreatExpense";
import ShowGroups from "./ShowGroups";
import ShowExpense from "./ShowExpense";
import { BrowserRouter as Router, Routes, Switch, Route, Link, Redirect } from "react-router-dom";


const HomePage = () => {

    return (
      <Router>
        <Routes>
          <Route exact path="/" element={<div>
      <h1>Splitter Home Page</h1>
      <Link to="/create">
        <button>Create User</button>
      </Link>
      <Link to="/creategroup">
        <button>Create Group</button>
      </Link>
      <Link to="/createexpense">
        <button>Create Expense</button>
      </Link>
      <Link to="/showgroups">
        <button>Groups</button>
      </Link>
      <Link to="/showexpense">
        <button>Debts</button>
      </Link>
    </div>
} />
          <Route path="/create" element={<CreateUser />} />
          <Route path="/creategroup" element={<CreateGroup />} />
          <Route path="/createexpense" element={<CreateExpense />} />
          <Route path="/showgroups" element={<ShowGroups />} />
          <Route path="/showexpense" element={<ShowExpense />} />
        </Routes>
      </Router>
    );
  };
  
  export default HomePage;