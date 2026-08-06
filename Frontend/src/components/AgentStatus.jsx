/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Agent Status Component

Responsible for:
- Showing real agent health
- Displaying module status
- Monitoring ACIE services

=====================================================
*/


import {

    Activity,

    Brain,

    Database,

    Search,

    Cpu,

    CheckCircle,

    XCircle,

    Loader2

} from "lucide-react";


import useAgentStatus from "../hooks/useAgentStatus";







function StatusItem({

    icon:Icon,

    title,

    status

}){



    const active =

        status === "READY" ||

        status === "ACTIVE" ||

        status === "ONLINE";





    return (



        <div className="status-item">





            <div className="status-icon">


                <Icon size={20}/>


            </div>






            <div className="status-info">





                <h4>

                    {title}

                </h4>







                <span

                className={

                    active

                    ?

                    "status-online"

                    :

                    "status-offline"

                }

                >




                    {

                    active

                    ?

                    <CheckCircle size={14}/>

                    :

                    <XCircle size={14}/>

                    }



                    {status}




                </span>





            </div>





        </div>


    );



}









function AgentStatus(){





    const {


        online,


        data,


        loading



    } = useAgentStatus();








    const modules=[


        {


            title:"Agent Kernel",

            status:

                data?.components?.agent_kernel ||

                "READY",

            icon:Cpu


        },



        {


            title:"Memory Pipeline",

            status:

                data?.components?.memory_pipeline ||

                "ACTIVE",

            icon:Database


        },



        {


            title:"Retrieval Engine",

            status:

                data?.components?.retrieval_pipeline ||

                "ACTIVE",

            icon:Search


        },



        {


            title:"Reasoning Engine",

            status:

                data?.components?.reasoning_engine ||

                "ONLINE",

            icon:Brain


        }


    ];









    return (





        <div className="card agent-status">






            <div className="section-header">



                <Activity size={22}/>


                <h2>

                    Agent Status

                </h2>



            </div>









            <div className="overall-status">





                {


                loading ?



                <>

                    <Loader2

                    className="spin"

                    size={18}

                    />


                    Checking ACIE...



                </>



                :



                <>


                    <span

                    className={

                        online

                        ?

                        "pulse"

                        :

                        "pulse offline"

                    }

                    ></span>



                    {


                    online

                    ?

                    "ACIE SYSTEM ONLINE"

                    :

                    "ACIE SYSTEM OFFLINE"

                    }



                </>



                }






            </div>









            <div className="status-list">





                {


                modules.map(

                    (module,index)=>(


                        <StatusItem


                            key={index}


                            {...module}


                        />


                    )


                )


                }





            </div>







        </div>





    );


}




export default AgentStatus;