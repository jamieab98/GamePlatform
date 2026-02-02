import {Link} from 'react-router-dom'
import LandingPage from './LandingPage'
import GameSelection from './GameSelection'
function NavigationBar(){

    return(
        <>
            <Link to="/" element={<LandingPage/>}>Home</Link>
            <Link to="/gameselection" element={<GameSelection/>}>Game Selection</Link>
        </>
    )
}
export default NavigationBar