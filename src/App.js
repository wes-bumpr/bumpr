import "./static/style.css";
import { useState } from 'react'
import axios from "axios";
import { Navbar } from "./components/Navbar.js";
import { AllForm } from "./components/AllForm.js";
import { RideRequest } from "./components/Request.js";
import { GoogleProvider } from "leaflet-geosearch";
import React from "react";
import {rideRequest} from "./utils.js";


export default function App() {

  const provider = new GoogleProvider({
    params: {
      apiKey: 'AIzaSyAouxsv_Fxccs3lakln7RNb9fz5h8Bs7aw',
      language: "en",
      region: "us",
    },
  });
  const [disable, setDisable] = React.useState(false);
  const [pax, setPax] = React.useState();
  const [coords, setCoords] = React.useState();
  const [toCoords, setToCoords] = React.useState();
  const [text, setText] = React.useState([]);
  const [toText, setToText] = React.useState([]);
  const [searchResults, setSearchResults] = React.useState([]);
  const [searchResultsTo, setSearchResultsTo] = React.useState([]);
  const [isSubmit, setSubmit] = React.useState(false);
  const [startDate, setStartDate] = React.useState(new Date());
  const address = React.useRef(null);
  const toAddress = React.useRef(null);
  const [sAddress, setsAddress] = React.useState('No address selected');
  const [sToAddress, setsToAddress] = React.useState('No address selected');
  const [formData, setFormData] = React.useState({
    timing: "",
    from_address: "",
    to_address: "",
    num_passengers: 0,
    from_coords: {'x':0, 'y':0},
    to_coords: {'x':0, 'y':0}
  });

  async function autocomplete(a) {
    setText(a);
    const results = await provider.search({ query: text });
    setSearchResults(results);
  }

  async function autocompleteTo(a) {
    setToText(a);
    const results = await provider.search({ query: toText });
    setSearchResultsTo(results);
  }

  function addressSelect(label, x, y) {
    setText(label)
    setCoords({'x':x,'y':y})
    setsAddress(label)
    setDisable(false)
  }

  function paxFill(num) {
    setPax(num.target.value.replace(/\D/,''))
    if ((num.target.value.replace(/\D/,'')).length > 0) {
      setDisable(false);
    } else {
      setDisable(true)
    }
  }

  function addressSelectTo(label, x, y) {
    setToText(label)
    setToCoords({'x':x,'y':y})
    setsToAddress(label)
    setDisable(false)
  }

  React.useEffect(() => {rideRequest(formData)}, [formData]);

  function submitHandler() {
    setFormData({
      timing: startDate.toLocaleString(),
      from_address: sAddress,
      from_coords: coords,
      num_passengers: pax,
      to_address: sToAddress,
      to_coords: toCoords,
    });
    setSubmit(true);
  }
  React.useEffect(() => {rideRequest(formData)}, [formData]);


  const [profileData, setProfileData] = useState(null)
  function getData() {
    axios({
      method: "GET",
      url:"/profile",
    })
    .then((response) => {
      const res =response.data
      setProfileData(({
        profile_name: res.name,
        about_me: res.about}))
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}

  return (
    <>
      <Navbar />
      {isSubmit ? (
        <RideRequest formData={formData} />
      ) : (
        <AllForm
          startDate={startDate}
          setStartDate={setStartDate}
          address={address}
          text={text}
          setText={setText}
          toAddress={toAddress}
          toText={toText}
          setToText={setToText}
          searchResults={searchResults}
          setSearchResults={setSearchResults}
          searchResultsTo={searchResultsTo}
          setSearchResultsTo={setSearchResultsTo}
          autocomplete={autocomplete}
          autocompleteTo={autocompleteTo}
          submitHandler={submitHandler}
          setCoords={setCoords}
          addressSelect={addressSelect}
          sAddress={sAddress}
          setToCoords={setToCoords}
          addressSelectTo={addressSelectTo}
          sToAddress={sToAddress}
          pax = {pax}
          setPax={setPax}
          disable={disable}
          setDisable={setDisable}
          paxFill={paxFill}
        />
      )}

    </>
  );
}
