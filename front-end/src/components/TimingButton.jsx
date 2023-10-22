import React from 'react';

export function TimingButton(){
    const [isNow, setNow] = React.useState("Now");

    const handleNow = () => {
        setNow("Now")
    };

    const handleLater = () => {
        setNow("Later")
    };

    const buttonStyle = {
        color: "black",
        backgroundColor: "#88D2F1", //todo ella figure out the correct color name
        borderRadius: 50,
        border: "none",
        fontSize: 30, //todo ella check if they have a particular size in mind
        fontFamily: "Karla", //todo ella check which font they want for buttons
        display: "inline-block",
        margin: "10px",
        padding: "10px 65px", //todo ella atm the later box is slightly longer cuz later is longer word
        boxShadow: "0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)",
    };

    const TimingButton = ({ onClick, children }) => {
        return (
        <button type="button" onClick={onClick} style={buttonStyle}>
            {children}
        </button>
        )
    };

    return (
        <div>
            <TimingButton onClick={handleNow}>Now</TimingButton>
            <TimingButton onClick={handleLater}>Later</TimingButton>
            {/* todo ella figure out how were dealing with forms, rn this just shows text when now is selected */}
            {/* {isNow && <div>Booking for now</div>}  */}
        </div>
        )
    }
