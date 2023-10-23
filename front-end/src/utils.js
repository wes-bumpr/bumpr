const SERVER_ORIGIN = '';
 
const rrUrl = `${SERVER_ORIGIN}/ride-request`;
 
export function rideRequest(data) {
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