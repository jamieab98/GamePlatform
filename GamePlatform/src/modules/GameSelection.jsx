import {useState} from 'react'

function GameSelection(){
    const [game, setGame] = useState("Select Game")
    function gameselect(){
        if(game == 'Select Game'){
            console.log('Please select a game')
        }
        else{
            console.log(game)
        }
    }

    return(
        <>
            <h3>Game Selection</h3>
            <select value={game} onChange={(e)=>setGame(e.target.value)} id='game'>
                <option value='Select Game'>--Select Game--</option>
                <option value='tic-tac-toe'>Tic-Tac-Toe</option>
                <option value='connect four'>Connect Four</option>
            </select>
            <button onClick={gameselect}>Select Game</button>
        </>
    )
}

export default GameSelection