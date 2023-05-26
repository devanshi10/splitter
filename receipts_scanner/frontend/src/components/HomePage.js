import React, { Component } from "react";
import CreateUser from "./CreateUser";
import CreateGroup from "./CreateGroup";
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
    </div>
} />
          <Route path="/create" element={<CreateUser />} />
          <Route path="/creategroup" element={<CreateGroup />} />
        </Routes>
      </Router>
    );
  };
  
  export default HomePage;