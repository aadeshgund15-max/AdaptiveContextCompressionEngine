/*
=====================================================

ACIE Frontend

useAgentStatus Hook

Responsible for:
- Checking backend status
- Tracking agent availability

=====================================================
*/


import {
    useEffect,
    useState
} from "react";


import {
    getAgentStatus
} from "../api/client";





function useAgentStatus(){


    const [status,setStatus] = useState({

        online:false,

        data:null

    });



    const [loading,setLoading] = useState(true);





    const checkStatus = async()=>{


        try{


            const response = await getAgentStatus();



            setStatus({

                online:true,

                data:response

            });



        }

        catch(error){


            setStatus({

                online:false,

                data:null

            });


        }


        finally{


            setLoading(false);


        }


    };






    useEffect(()=>{


        checkStatus();



        const interval = setInterval(

            checkStatus,

            30000

        );



        return ()=>clearInterval(interval);



    },[]);






    return {


        ...status,

        loading,

        refresh:checkStatus


    };


}



export default useAgentStatus;