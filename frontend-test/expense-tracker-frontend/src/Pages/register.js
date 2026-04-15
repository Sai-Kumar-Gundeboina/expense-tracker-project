import { useState } from "react";

function Register(props){
    // const [age, setAge] = useState(0);
    const[employees, setEmp] = useState([]);
    const[name, setName]= useState('');
    const[id, setId] = useState(0);

    const removeEmp=(idx)=>{
        const updatedEmp = employees.filter((_, i)=>i!==idx)
        setEmp(updatedEmp);
    }
    return (<div>
        <h1>hello</h1>
       <h2>Employee addition </h2>

       {/* <label>Current count: {age}</label>
       <br></br>
       <button onClick={()=> {setAge(age+1)}}>increase</button>
       <button onClick={()=> {setAge(0)}}>Make Zero</button> */}

        <label>Name : </label>
        <input type="text" value={name} onChange={(a)=>setName(a.target.value)}></input>
        <br></br>
        <label>ID :  </label>
        <input type="int" value={id} onChange={(a) => setId(a.target.value)}></input>
        <br></br>
        <button onClick={()=> {setEmp([...employees, [name, id]]); setId(0);setName('')}}
        >Add</button>
        <br></br>
        <div>
            {employees.map((row, rowIndex) => (
                <div key={rowIndex}>
                {row.map((col, colIndex) => (
                    <span key={colIndex} style={{ margin: "10px" }}>
                    {col}
                    </span>
                ))}
                <button onClick={() => removeEmp(rowIndex)}>remove</button>
                </div>
            ))}
        </div>
    </div>)
}
export default Register;