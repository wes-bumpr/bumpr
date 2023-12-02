import { useState } from 'react'
import axios from "axios";



const SERVER_ORIGIN = '';
const rrUrl = "/ride-request";
export async function rideRequest(data) {
  // param data: a list of dictionary ride requests
  // example: ride_requests = [{"depart_time": 1000, "user_ID": "C1024851", "destination_address": {"city": "Needham", "state": "MA"}},
  //                          {"depart_time": 1050, "user_ID": "C1000001", "destination_address": {"city": "Wellesley", "state": "MA"}}]
 
console.log(data)
return axios({
  method: "POST",
  url: "/ride-request",
  data:
    data,
})
  .then((response) => {
    const res = response.data;
    console.log('Request successful:', res);
    return res;
  })
  .catch((error) => {
    if (error.response) {
      console.log('Request failed:', error.response.status);
      console.log('Response data:', error.response.data);
      console.log('Response headers:', error.response.headers);
    }
  });
}
