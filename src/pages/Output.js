import React, { useEffect, useState } from "react";
import { useLocation } from 'react-router-dom';
export const Output = () => {
    const location = useLocation();
    const [formData, setFormData] = useState(null);
    const [profileData, setProfileData] = useState(null);


    useEffect(() => {
        if (location.state && location.state.formData && location.state.profileData) {
            setFormData(location.state.formData)
            setProfileData(location.state.profileData)
        }
    }, [location.state]);

    // const {formData, profileData} = location.state;
        if (profileData == "No Match") {
        return (
        <div class="container">
            <div class="prompt mb-5">
            You did not match with anyone.
            We will notify you if you receive a new match before your date.
            </div>
        </div>
        )} else if (profileData) { 
            return (
            <div class="container">
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
                {/* <button type="button" class="btn btn-info mt-5 contbutton" onClick={setContinue}>Continue</button> */}
                </div>
                </div>
            </div>
            </div>
        )}
    else {
        return (
        <div class="prompt mb-5">error retrieving match data: {profileData}</div>
        )
    }
    }
