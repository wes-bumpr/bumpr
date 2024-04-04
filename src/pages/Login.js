import React, { useState } from 'react';
import axios from "axios";



export const Login = () => {
  const [isSubmit, setSubmit] = useState(false);
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

  React.useEffect(() => {
    if (isSubmit) {
      console.log(formData)
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
  }
  }, [isSubmit]);

  return (
    <div>
      <h2>User Information</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Email:</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Phone:</label>
          <input
            type="tel"
            name="phone_number"
            value={formatPhoneNumber(formData.phone_number)}
            onChange={handleChange}
            placeholder="Format: 123-456-7890"
            required
          />
        </div>
        <button type="submit" onClick={setSubmit}>Submit</button>
      </form>
    </div>
  );
}

