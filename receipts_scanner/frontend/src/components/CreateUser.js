import React, { useState } from "react";

const CreateUser = () => {
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [password, setPassword] = useState("");


  const handleSubmit = async (e) => {
    e.preventDefault();


    try {
        const response = await fetch("/myApp/userprofile", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",


          },
          body: JSON.stringify({
            email,
            first_name: firstName,
            last_name: lastName,
            password,
          }),
        });
  
        if (response.ok) {
          // User created successfully
          // Redirect to a success page or perform any necessary actions
          setEmail("");
          setFirstName("");
          setLastName("");
          setPassword("");

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
      <h1>Create User</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label>First Name:</label>
          <input
            type="text"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Last Name:</label>
          <input
            type="text"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Create User</button>
      </form>
    </div>
  );
};

export default CreateUser;
