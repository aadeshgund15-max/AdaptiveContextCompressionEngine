/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Evaluation Page

Responsible for:
- System performance analysis
- Compression evaluation
- AI metrics monitoring

=====================================================
*/


import {


    motion


} from "framer-motion";


import {


    BarChart3,

    TrendingDown,

    Database,

    Gauge,

    Target


} from "lucide-react";


import MetricsCard from "../components/MetricsCard";








function Evaluation(){





    const evaluationMetrics=[





        {


            title:"Compression Ratio",


            value:"72%",


            description:
            "Average context compression achieved",


            type:"compression"



        },





        {


            title:"Token Reduction",


            value:"65%",


            description:
            "Reduction in LLM context tokens",


            type:"token"



        },





        {


            title:"Memory Efficiency",


            value:"89%",


            description:
            "Relevant memory retrieval accuracy",


            type:"memory"



        },





        {


            title:"Reasoning Score",


            value:"94%",


            description:
            "Agent reasoning confidence",


            type:"confidence"



        }



    ];









    const evaluationStages=[





        {


            name:"Context Compression",


            score:92,


            icon:TrendingDown



        },






        {


            name:"Memory Retrieval",


            score:88,


            icon:Database



        },






        {


            name:"Reasoning Quality",


            score:94,


            icon:Target



        },






        {


            name:"Response Performance",


            score:90,


            icon:Gauge



        }





    ];













    return (







        <motion.div





            className="evaluation-page"





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



                    ACIE Evaluation



                </h1>







                <p>



                    Analyze intelligence performance and optimization metrics



                </p>






            </div>













            {/* Metrics */}







            <div className="metrics-grid">





            {


            evaluationMetrics.map((metric,index)=>(





                <MetricsCard





                    key={index}





                    {...metric}





                />





            ))





            }





            </div>
















            {/* Pipeline Evaluation */}





            <div className="evaluation-panel">







                <div className="panel-title">





                    <BarChart3 size={24}/>





                    <h2>



                        Pipeline Evaluation



                    </h2>





                </div>









                <div className="evaluation-list">







                {


                evaluationStages.map((stage,index)=>{






                    const Icon = stage.icon;







                    return (








                    <motion.div





                        key={index}





                        className="evaluation-item"





                        initial={{


                            opacity:0,


                            x:-20



                        }}



                        animate={{


                            opacity:1,


                            x:0



                        }}



                        transition={{


                            delay:index*0.1


                        }}



                    >







                        <div className="evaluation-icon">



                            <Icon size={22}/>



                        </div>









                        <div className="evaluation-content">





                            <h3>



                                {stage.name}



                            </h3>







                            <div className="score-row">





                                <span>



                                    Score



                                </span>





                                <strong>



                                    {stage.score}%



                                </strong>





                            </div>









                            <div className="progress-bar">





                                <motion.div





                                    className="progress-fill"





                                    initial={{width:0}}



                                    animate={{



                                        width:`${stage.score}%`



                                    }}



                                    transition={{


                                        duration:0.8


                                    }}



                                />





                            </div>







                        </div>







                    </motion.div>









                    );






                })






                }







                </div>







            </div>












            {/* Chart Section */}







            <div className="chart-placeholder">





                <h2>



                    Performance Visualization



                </h2>







                <p>



                    Charts will be connected with ACIE evaluation API.



                </p>







            </div>








        </motion.div>







    );


}







export default Evaluation;