import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import data from './db.json';
import Top from './Top';
import Button from './Button';


let logo = "https://cdn-icons-png.flaticon.com/512/5625/5625755.png";
let title = "10 лучших фильмов по версии Кинопоиска";
let slogan = "Лучшие из лучших";
let torrent = "СКАЧАТЬ БЕСПЛАТНО НА ВЫСОКОЙ СКОРОСТИ"
let poster = [
  "https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_FMjpg_UX500_.jpg",
  "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_FMjpg_UX500_.jpg",
  "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_FMjpg_UX500_.jpg",
  "https://avatars.mds.yandex.net/get-kinopoisk-image/6201401/97ed7256-db80-4532-ab6b-6688d2eab4b2/1920x",
  "https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_FMjpg_UX500_.jpg",
  "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_FMjpg_UX500_.jpg",
  "https://images-s.kinorium.com/movie/poster/139945/w1500_49879866.jpg",
  "https://m.media-amazon.com/images/M/MV5BNDIzNDU0YzEtYzE5Ni00ZjlkLTk5ZjgtNjM3NWE4YzA3Nzk3XkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_FMjpg_UX500_.jpg",
  "https://m.media-amazon.com/images/M/MV5BMTUxMzQyNjA5MF5BMl5BanBnXkFtZTYwOTU2NTY3._V1_FMjpg_UX500_.jpg",
  "https://i.pinimg.com/originals/a9/99/b6/a999b676132d88b2d82ad7bfc44ca382.jpg"

];
let db = data.films;



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App slogan={slogan} title={title}  logo={logo} />
    <Top poster={poster} db={db} />
    <Button torrent={torrent}/>
    
  </React.StrictMode>
);
