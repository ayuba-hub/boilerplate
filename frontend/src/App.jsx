import Footer from './components/Footer';
import Hompage from './components/Hompage';
import { Link } from 'react-router-dom';

function App() {
  return (
    <div>

      <div className="d-flex border py-4 mb-2"></div>
      
     <div className='container border-bottom'>
     <nav className='navbar navbar-expand-md'>
      <div className="navbar-brand">
        <Link className='nav-link' to='#'>
          LinkMart Logo
        </Link>
      </div>
        <button 
          className="navbar-toggler"
          type='button'
          data-bs-toggle='collapse'
          data-bs-target='#mobileToggler'
          aria-controls='mobileToggler'
          aria-expanded='false'
          aria-label='Toggle navigation'
        >
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id='mobileToggler'>
          <ul className='navbar-nav ms-auto text-center'>

            <li>
              <div className="input-group mt-2">
                <input className='form-control' placeholder='Search Product or Category' type="text" name="" id="" />
                <button className="input-group-text">
                  <i className="bi bi-search"></i>
                </button>
              </div>
            </li>
        
            <li>
              <Link className='nav-link' to='#'>Cart</Link>
            </li>
            <li>
              <Link className='nav-link' to='#'>Login</Link>
            </li>
            <li>
              <Link className='nav-link' to='#'>SignUp</Link>
            </li>
            <li>
              <Link className='nav-link' to='#'>Products</Link>
            </li>
            <li>
              <Link className='nav-link' to='#'>Contact</Link>
            </li>
          </ul>
        </div>
     </nav>
     Ads can be added here
    </div>
    <Hompage/>
    </div>
  );
}

export default App;
