/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Memory Page

Responsible for:
- Agent memory visualization
- Stored knowledge monitoring
- Memory intelligence overview

=====================================================
*/


import {


    motion


} from "framer-motion";



import {


    Database,

    Brain,

    Activity,

    Search,

    Layers


} from "lucide-react";



import MemoryPanel from "../components/MemoryPanel";

import MetricsCard from "../components/MetricsCard";









function Memory(){






    const memoryMetrics=[





        {


            title:"Total Memories",


            value:"128",


            description:
            "Stored agent experiences",


            type:"memory"



        },





        {


            title:"Retrieval Accuracy",


            value:"91%",


            description:
            "Relevant memory matches",


            type:"confidence"



        },





        {


            title:"Memory Activity",


            value:"ACTIVE",


            description:
            "Continuous learning enabled",


            type:"activity"



        }





    ];













    const memoryFeatures=[





        {


            title:"Semantic Memory",


            description:
            "Stores meaningful long-term knowledge",


            icon:Brain



        },





        {


            title:"Context Memory",


            description:
            "Maintains current conversation state",


            icon:Layers



        },





        {


            title:"Memory Retrieval",


            description:
            "Finds relevant information using embeddings",


            icon:Search



        },





        {


            title:"Memory Optimization",


            description:
            "Compresses redundant information",


            icon:Activity



        }





    ];















    return (







        <motion.div





            className="memory-page"





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







            <div className="page-header">





                <h1>



                    ACIE Memory System



                </h1>








                <p>



                    Manage and analyze adaptive agent memory



                </p>






            </div>













            {/* Memory Metrics */}





            <div className="metrics-grid">





            {


            memoryMetrics.map((metric,index)=>(





                <MetricsCard





                    key={index}





                    {...metric}





                />





            ))





            }





            </div>
















            {/* Main Memory Area */}






            <div className="memory-layout">







                <div>



                    <MemoryPanel/>




                </div>













                <motion.div





                    className="memory-features"





                    initial={{


                        opacity:0,


                        x:30



                    }}



                    animate={{


                        opacity:1,


                        x:0



                    }}



                >







                    <h2>



                        Memory Intelligence



                    </h2>









                    {


                    memoryFeatures.map((feature,index)=>{





                        const Icon=feature.icon;







                        return (







                            <motion.div





                                key={index}





                                className="feature-card"





                                whileHover={{


                                    scale:1.03



                                }}



                                transition={{


                                    duration:0.2


                                }}



                            >







                                <div className="feature-icon">



                                    <Icon size={22}/>



                                </div>









                                <div>







                                    <h3>



                                        {feature.title}



                                    </h3>







                                    <p>



                                        {feature.description}



                                    </p>






                                </div>







                            </motion.div>








                        );





                    })






                    }







                </motion.div>







            </div>













            {/* Knowledge Graph */}





            <motion.div





                className="knowledge-section"





                whileHover={{


                    scale:1.01



                }}






            >







                <Database size={24}/>







                <div>







                    <h2>



                        Knowledge Graph



                    </h2>







                    <p>



                        Graph based memory visualization will be integrated here.



                    </p>







                </div>







            </motion.div>









        </motion.div>







    );





}






export default Memory;