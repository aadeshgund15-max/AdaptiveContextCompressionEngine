/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Reasoning Trace Component

Responsible for:
- Showing agent reasoning pipeline
- Displaying execution flow
- Tracking AI processing stages

=====================================================
*/


import {


    Search,

    Brain,

    Database,

    MessageSquare,

    Sparkles,

    CheckCircle,

    Loader2,

    Circle


} from "lucide-react";



import {


    motion


} from "framer-motion";









function ReasoningStep({


    icon:Icon,

    title,

    description,

    status="completed",

    index



}){





    const completed = status === "completed";



    const running = status === "running";







    return (





        <motion.div





            className="reasoning-step"





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







            <div className={

                running

                ?

                "reasoning-icon active"

                :

                "reasoning-icon"

            }>




                <Icon size={20}/>





            </div>









            <div className="reasoning-content">





                <h3>



                    {title}



                </h3>







                <p>



                    {description}



                </p>









                <span





                className={

                    completed

                    ?

                    "step-completed"

                    :

                    running

                    ?

                    "step-running"

                    :

                    "step-pending"

                }





                >





                    {


                    completed

                    ?

                    <CheckCircle size={14}/>


                    :


                    running


                    ?

                    <Loader2 size={14}/>


                    :


                    <Circle size={14}/>




                    }






                    {status}





                </span>








            </div>









        </motion.div>





    );



}









function ReasoningTrace({trace=[]}){





    const defaultSteps=[





        {


            title:"Context Compression",


            description:

            "Analyzing and compressing user context",


            icon:Database,


            status:"completed"


        },







        {


            title:"Memory Retrieval",


            description:

            "Searching relevant stored memories",


            icon:Search,


            status:"completed"


        },








        {


            title:"Reasoning Engine",


            description:

            "Generating logical reasoning path",


            icon:Brain,


            status:"running"


        },








        {


            title:"Response Generation",


            description:

            "Creating final AI response",


            icon:MessageSquare,


            status:"pending"


        }





    ];








    const steps =

        trace.length > 0

        ?

        trace

        :

        defaultSteps;









    return (





        <div className="reasoning-trace">







            <div className="trace-header">





                <Sparkles size={22}/>




                <h2>

                    Reasoning Trace

                </h2>





            </div>









            <div className="trace-container">








            {


            steps.map((step,index)=>(





                <ReasoningStep





                    key={index}




                    index={index}




                    icon={

                        step.icon ||

                        Brain

                    }



                    title={step.title}




                    description={step.description}




                    status={

                        step.status ||

                        "completed"

                    }





                />





            ))





            }







            </div>







        </div>





    );




}






export default ReasoningTrace;