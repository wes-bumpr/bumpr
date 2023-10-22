import "./static/style.css";
import { Navbar } from "./components/Navbar.js";
import { AllForm } from "./components/AllForm.js";
import { RideRequest } from "./components/Request.js";
import React from "react";



export default function App() {
  const [isSubmit, setSubmit] = React.useState(false);
  const [startDate, setStartDate] = React.useState(new Date());
  const address = React.useRef(null);
  const [formData, setFormData] = React.useState({
    timing: '',
    address: '',
  });

  const submitSetter = React.useCallback(
    (val) => {
      setSubmit(val);
    },
    [setSubmit]
  );

  return (
    <>
      <Navbar />
      {isSubmit ? (
        <RideRequest formData={formData} />
      ) : (
        <AllForm
          isSubmit={isSubmit}
          setSubmit={submitSetter}
          formData={formData}
          setFormData={setFormData}
          startDate={startDate}
          setStartDate={setStartDate}
          address={address}
        />
      )}

    </>
  );
}
