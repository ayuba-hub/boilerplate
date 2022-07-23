import Footer from './components/Footer';
import Header from './components/Header';
import Hompage from './components/Hompage';
import { Link } from 'react-router-dom';

function App() {
  return (
    <div>
     <header
     className='
     border bottom
     py-3
     mb-2
     d-flex
     flex-wrap
     justify-content-center
     '
     >
      header1
     </header>

     <nav className='container border-bottom py-4 mb-2 d-flex flex-wrap'>

      <div className="dropdown">
        <button className="btn btn-secondary" id='nav_dropdown' data-bs-toggle='dropdown' aria-haspopup='true'>
          <i className="bi bi-justify"></i>
        </button>
        <div className="dropdown-menu" aria-labelledby='nav_dropdown'>
          <ul className='list-unstyled mt-2 text-center'>
            <li><Link className='nav nav-link' to="#">Item 1</Link></li>
            <li><Link className='nav nav-link' to="#">Item 1</Link></li>
            <li><Link className='nav nav-link' to="#">Item 1</Link></li>
            <li><Link className='nav nav-link' to="#">Item 1</Link></li>
            <li><Link className='nav nav-link' to="#">Item 1</Link></li>
            <li><Link className='nav nav-link' to="#">Item 1</Link></li>
            <li><Link className='nav nav-link' to="#">Item 1</Link></li>                    
          </ul>
        </div>
      </div>

      <div className="input-group">
        <input className='form-control' type="text" name="search" id="search" />
        <button className="input-group-text">
          <i className='bi bi-search'></i>
          </button>
      </div>
      
     </nav>
    </div>
  );
}

export default App;
