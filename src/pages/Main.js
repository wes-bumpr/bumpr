// export const Main = () => {
//     return (
//         <h1>Main page, we routed!</h1>
//     );
// }


import "../static/style.css";
import { useState } from 'react'
import axios from "axios";
import { Navbar } from "../components/Navbar.js";
import { AllForm } from "../components/AllForm.js";
import { RideResult } from "../components/Result.js";
import { RideRequest } from "../components/Request.js";
import { GoogleProvider } from "leaflet-geosearch";
import React from "react";
import {rideRequest} from "../utils.js";
import { Link } from "react-router-dom";
// import { useNavigate } from "react-router-dom";
// import ResultList from "leaflet-geosearch/dist/resultList";


export default function Main() {

  const provider = new GoogleProvider({
    params: {
      apiKey: 'AIzaSyAouxsv_Fxccs3lakln7RNb9fz5h8Bs7aw',
      language: "en",
      region: "us",
    },
  });


//   let navigate = useNavigate(); 
//   const routeChange = () =>{ 
//     let path = `/output`; 
//     navigate(path);
//   }

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
    depart_time: "",
    origin_address: "",
    destination_address: "",
    total_num_people_traveling: 0,
    origin_geocode: {'longitude':0, 'latitude':0},
    destination_geocode: {'longitude':0, 'latitude':0},
    user_ID: "C10012147",
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
    setCoords({'longitude':x,'latitude':y})
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
    setToCoords({'longitude':x,'latitude':y})
    setsToAddress(label)
    setDisable(false)
  }


  function submitHandler() {
    setFormData({
      depart_time: startDate.toLocaleString(),

      origin_address: sAddress,
      origin_geocode: coords,
      total_num_people_traveling: Number(pax),
      destination_address: sToAddress,
      destination_geocode: toCoords,
      user_ID: "testing1",
    });
    setSubmit(true);
  }

  

  const [profileData, setProfileData] = React.useState(null);


  React.useEffect(() => {if (isSubmit) {
    const fetchData = async () => {
      try {
        console.log("form data in main.js" + formData)
        const requestResult = await rideRequest(formData); // Assuming rideRequest returns a Promise
        console.log("request result", requestResult)
        setProfileData(requestResult)
        console.log("request result in main.js" + requestResult)
        console.log("set formData ", formData)
        //setProfileData(requestResult); // Update state with the result of rideRequest
        console.log("setprofiledata" + profileData)
      } catch (error) {
        // Handle errors if necessary
        console.error('Error:', error);
      }
    };
    fetchData();} // Call the async function to fetch data when formData changes
  }, [isSubmit]);

  
  // function getData() {
  //   axios({
  //     method: "GET",
  //     url:"/profile",
  //   })
  //   .then((response) => {
  //     const res =response.data
  //     setProfileData(({
  //       profile_name: res.name,
  //       about_me: res.about}))
  //   }).catch((error) => {
  //     if (error.response) {
  //       console.log(error.response)
  //       console.log(error.response.status)
  //       console.log(error.response.headers)
  //       }
  //   })
  // }
//           <RideResult formData={formData} profileData={profileData}></RideResult>


  return (
    <>
      <Navbar />
      {isSubmit ? (
          <Link to={{pathname: "/input", state: {formData, profileData}}}><button>
          View Match 
        </button>
        </Link>
        // isContinue ? (
        //   <RideRequest formData={formData} />
        // ) : (
        //   <RideResult formData={formData} profileData = {profileData} />
        // ) 
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
