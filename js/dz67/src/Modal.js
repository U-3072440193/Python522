import './Modal.css';
import {useState} from "react";

function Modal() {
  let [open, setOpen] = useState(false);
  let image = "https://user-images.githubusercontent.com/131547083/234182208-0ebdd2ed-8ef8-4060-94e9-a0865cfa5696.jpg";

  return (
    <div>
      <img
        src={image}
        alt=""
        className="small"
        onClick={() => setOpen(true)}
        style={{ display: open ? "none" : "block" }}
      />
      {open && (
        <div>
          <img src={image} alt="" className="big" onClick={()=> setOpen(false)}/>
        </div>
      )}
    </div>
  );
}

export default Modal;