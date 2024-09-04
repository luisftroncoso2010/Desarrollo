import './App.css';
import {useRef} from 'react'
import video from './assets/video.mp4'


function App() {
/* Usamos el Hooks useReft */
  const videoRef = useRef(null)

  const videoPlay = () =>{
    videoRef.current.play()
  }

  const videoPause = () => {
    videoRef.current.pause()
  }

  return (
    <div className="App">

      <video ref={videoRef} width="400px">
        <source src={video} type='video/mp4'></source>
      </video>

      <div>
        
        <button onClick={videoPlay}>Play</button>
        <button onClick={videoPause}>Pausa</button>
      </div>

    </div>
  );
}

export default App;
