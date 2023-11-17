import logo from '../static/assets/logo.png';

export function Navbar() {
    return(
        <nav>
            <span className="logo">
                bumpr
                <img className="vLogo" src={logo} alt="Logo"></img>
            </span>
        </nav>
    )
}