/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Dashboard Page

Responsible for:
- Agent overview
- System metrics
- Intelligence monitoring

=====================================================
*/


import {

    motion

} from "framer-motion";


import AgentStatus from "../components/AgentStatus";

import MetricsCard from "../components/MetricsCard";

import ReasoningTrace from "../components/ReasoningTrace";


import {


    Database,

    Zap,

    Brain


} from "lucide-react";








function Dashboard(){





    const metrics=[





        {


            title:"Compression Ratio",


            value:"72%",


            description:"Context optimization achieved",


            type:"compression"



        },






        {


            title:"Stored Memories",


            value:"128",


            description:"Long term agent memories",


            type:"memory"



        },






        {


            title:"Response Latency",


            value:"1.8s",


            description:"Average response time",


            type:"latency"



        },






        {


            title:"Agent Confidence",


            value:"94%",


            description:"Reasoning confidence score",


            type:"confidence"



        }




    ];









    const systemOverview=[






        {


            title:"Context Intelligence",


            icon:Brain,


            status:"ACTIVE"



        },






        {


            title:"Memory System",


            icon:Database,


            status:"ONLINE"



        },






        {


            title:"Execution Engine",


            icon:Zap,


            status:"READY"



        }







    ];









    return (








        <motion.div






            className="dashboard"






            initial={{


                opacity:0,


                y:20



            }}



            animate={{


                opacity:1,


                y:0



            }}



            transition={{


                duration:0.5


            }}





        >







            {/* Header */}





            <div className="page-header">





                <h1>


                    ACIE Dashboard



                </h1>








                <p>


                    Adaptive Context Intelligence Engine Monitoring Center



                </p>






            </div>















            {/* Metrics */}





            <motion.div





                className="metrics-grid"





                initial="hidden"

                animate="visible"

                variants={{


                    visible:{


                        transition:{


                            staggerChildren:0.1


                        }

                    }



                }}







            >






                {


                metrics.map((metric,index)=>(






                    <MetricsCard





                        key={index}





                        {...metric}





                    />






                ))





                }







            </motion.div>














            {/* Main Dashboard Grid */}





            <div className="dashboard-grid">







                <AgentStatus/>













                <motion.div





                    className="system-overview"





                    whileHover={{


                        scale:1.01



                    }}



                >








                    <h2>


                        System Overview



                    </h2>









                    {


                    systemOverview.map((item,index)=>{






                        const Icon=item.icon;







                        return (






                            <div





                            key={index}





                            className="overview-item"





                            >







                                <div className="overview-icon">





                                    <Icon size={22}/>





                                </div>









                                <div>







                                    <h3>

                                        {item.title}



                                    </h3>







                                    <span>



                                        ● {item.status}



                                    </span>







                                </div>







                            </div>








                        );






                    })






                    }







                </motion.div>








            </div>












            {/* Reasoning Preview */}





            <div className="reasoning-preview">





                <ReasoningTrace/>





            </div>







        </motion.div>







    );


}





export default Dashboard;