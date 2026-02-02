import {BrowserRouter, Routes, Route} from 'react-router-dom'
import LandingPage from './modules/LandingPage'
import NavigationBar from './modules/NavigationBar'
import GameSelection from './modules/GameSelection'

function App(){

  return(
    <BrowserRouter>
      <NavigationBar/>
      <Routes>
        <Route path="/" element={<LandingPage/>}/>
        <Route path="/gameselection" element={<GameSelection/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
