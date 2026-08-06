/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

useMetrics Hook

Responsible for:
- Dashboard metric management
- Fetching agent performance data
- Monitoring ACIE evaluation

=====================================================
*/


import {

    useEffect,

    useState

} from "react";


import {

    getMetrics

} from "../api/client";







function useMetrics(){



    const [metrics,setMetrics] = useState({



        compressionRatio:"0%",


        tokenReduction:"0%",


        memories:0,


        latency:"0ms",


        confidence:"0%"



    });





    const [loading,setLoading] = useState(false);



    const [error,setError] = useState(null);









    const fetchMetrics = async()=>{



        setLoading(true);


        setError(null);






        try{



            const response = await getMetrics();





            setMetrics({


                compressionRatio:

                    response.compressionRatio ||

                    "0%",




                tokenReduction:

                    response.tokenReduction ||

                    "0%",





                memories:

                    response.memories ||

                    0,





                latency:

                    response.latency ||

                    "0ms",





                confidence:

                    response.confidence ||

                    "0%"



            });




        }



        catch(err){



            console.error(

                "Metrics fetch error:",

                err

            );



            setError(

                err.message

            );




        }



        finally{



            setLoading(false);



        }



    };









    useEffect(()=>{



        fetchMetrics();



    },[]);









    return {



        metrics,


        loading,


        error,


        refresh:fetchMetrics



    };



}





export default useMetrics;