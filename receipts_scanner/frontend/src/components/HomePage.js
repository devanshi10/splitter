import React, { Component } from "react";
import CreateUser from "./CreateUser";
import { BrowserRouter as Router, Routes, Switch, Route, Link, Redirect } from "react-router-dom";


const HomePage = () => {
    return (
      <Router>
        <Routes>
          <Route path="/" element={<div>
      <h1>Splitter Home Page</h1>
      <Link to="/create">
        <button>Create User</button>
      </Link>
    </div>
} />
          <Route path="/create" element={<CreateUser />} />
        </Routes>
      </Router>
    );
  };
  
  export default HomePage;