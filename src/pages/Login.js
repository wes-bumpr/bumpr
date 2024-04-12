import React, { useState } from 'react';
import axios from "axios";
import {useNavigate} from "react-router-dom";
import { Navbar } from "../components/Navbar.js";


export const Login = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone_number: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
  };

  const formatPhoneNumber = (value) => {
    // Format the phone number (e.g., 123-456-7890)
    const cleaned = ('' + value).replace(/\D/g, '');
    const match = cleaned.match(/^(\d{3})(\d{3})(\d{4})$/);
    if (match) {
      return match[1] + '-' + match[2] + '-' + match[3];
    }
    return value;
  };

  const navigate = useNavigate()
  function handleClick() {
    axios({
      method: "POST",
      url: "/login",
      data:
        formData,
    }).catch((error) => {
      if (error.response) {
        console.log('Request failed:', error.response.status);
        console.log('Response data:', error.response.data);
        console.log('Response headers:', error.response.headers);
      }
    });
    navigate('/')
  }

  return (
    <>
    <Navbar />
    <div  class="middle">
      <h2>Welcome to</h2>
      <h1 class="prompt"> BUMPR!</h1>
      <h2>Please input your user information:</h2>
      
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:  </label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Email:  </label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Phone: </label>
          <input
            type="tel"
            name="phone_number"
            value={formatPhoneNumber(formData.phone_number)}
            onChange={handleChange}
            placeholder="Format: 123-456-7890"
            required
          />
        </div>
        <button type="button" onClick={handleClick} class="button-style">Submit</button>
      </form>
    </div>
    </>
  );
}

