import React, { useEffect, useState } from "react";
import { useLocation, Link } from 'react-router-dom';

export const Input = () => {
    const location = useLocation();
    const [formData, setFormData] = useState(null);
    const [profileData, setProfileData] = useState(null);


    useEffect(() => {
        if (location.state && location.state.formData && location.state.profileData) {
            setFormData(location.state.formData)
            setProfileData(location.state.profileData)
        }
    }, [location.state]);

    // while (formData == null) {
    //     console.log("waiting for form data")
    // }

    console.log("form data in Input", formData)
    // const {formData, profileData} = location.state;
        if (formData) {
        return (
            <div class="row promptholder align-items-center justify-content-center">
            <div class="row align-items-center justify-content-center">
              <div class="prompt mb-5">
                You have created the following ride request:
              </div>
              <div class="card px-0 ridereq">
                <div class="card-header">{formData["user_ID"]}</div>
                <ul class="list-group list-group-flush">
                  <div class="list-group-item">
                    <small>Departure Time</small>
                    <div class="mb-1">{formData["depart_time"]}</div>
                  </div>
                  <div class="list-group-item">
                    <small>Departure Address</small>
                    <div class="mb-1">{formData["origin_address"]}</div>
                  </div>
                  <div class="list-group-item">
                    <small>Destination Address</small>
                    <div class="mb-1">{formData["destination_address"]}</div>
                  </div>
                  <div class="list-group-item">
                    <small>Number of Passengers</small>
                    <div class="mb-1">{formData["total_num_people_traveling"]}</div>
                  </div>
                </ul>
              </div>
              <div class="row justify-content-center">
              <Link to={{pathname: "/output", state: {formData, profileData}}}><button>
                    View Match 
                 </button>
                </Link>
            </div>
            </div>
          </div>
        )} else {
            return (
                <div class="prompt mb-5">error collecting your ride data: {formData}</div>
            )
    }
    }
