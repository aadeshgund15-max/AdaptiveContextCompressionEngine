/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

useMemory Hook

Responsible for:
- Memory state management
- Fetching stored memories
- Refreshing memory data

=====================================================
*/


import {
    useEffect,
    useState
} from "react";


import {
    getMemories
} from "../api/client";






function useMemory(){



    const [memories,setMemories] = useState([]);



    const [loading,setLoading] = useState(false);



    const [error,setError] = useState(null);







    const fetchMemories = async()=>{



        setLoading(true);


        setError(null);




        try{



            const response = await getMemories();





            setMemories(


                response.memories ||

                response ||

                []



            );





        }



        catch(err){



            console.error(

                "Memory fetch error:",

                err

            );




            setError(

                err.message

            );



            setMemories([]);



        }



        finally{



            setLoading(false);



        }



    };









    useEffect(()=>{



        fetchMemories();



    },[]);









    const clearMemory=()=>{



        setMemories([]);



    };









    return {



        memories,


        loading,


        error,


        refresh:fetchMemories,


        clearMemory



    };



}





export default useMemory;