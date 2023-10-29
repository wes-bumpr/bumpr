const SERVER_ORIGIN = '';
 
const rrUrl = `${SERVER_ORIGIN}/ride-request`;
 
export function rideRequest(data) {
  // param data: a list of dictionary ride requests
  // example: ride_requests = [{"depart_time": 1000, "user_ID": "C1024851", "destination_address": {"city": "Needham", "state": "MA"}},
  //                          {"depart_time": 1050, "user_ID": "C1000001", "destination_address": {"city": "Wellesley", "state": "MA"}}]
  return fetch(rrUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
  }).then((response) => {
    if (response.status !== 200) {
      throw Error('Fail to make request');
    }
 
    return response.json();
  })
}