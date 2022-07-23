import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import { useState,useEffect } from 'react'
import {API} from '../Constants'


const Hompage = () => {

  const [category,setCategory] =  useState([])
  
 useEffect(()=>{
    axios.get(`${API}/category`).then(
      res=>{
        const categories= res.data
        setCategory(categories);
      }
    ).catch(error=>{
      console.log(error)
    })
  }
  ,[])
  return (
    <div className='container mt-4'>
     <div className="row">
      <div className="col-md-1 mt-2">
        <div className="dropdown">
          <button className="btn btn-secondary" data-bs-toggle='dropdown'>
            <i className="bi bi-justify"></i>
          </button>

          <div className="dropdown-menu">
            
              {category.map(cat=>{
                return(
                  
                    <li className='dropdown-item' key={cat.id}>
                      <Link className='nav-link' to={`categories/${cat.category}`}>{cat.category}</Link>
                    </li>
                  
                )
              })}
          </div>
        </div>
      </div>
      <div className="col-md">
        <div className="card card-body mt-2"></div>
      </div>
     </div>
    </div>
  )
}

export default Hompage