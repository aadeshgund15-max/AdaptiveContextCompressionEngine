/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Metrics Card Component

Responsible for:
- Displaying system metrics
- Reusable dashboard cards
- AI performance indicators

=====================================================
*/


import {

    TrendingUp,

    Database,

    Cpu,

    Clock,

    Brain,

    Activity

} from "lucide-react";


import {

    motion

} from "framer-motion";








const ICON_MAP = {



    compression:

        TrendingUp,



    memory:

        Database,



    token:

        Cpu,



    latency:

        Clock,



    confidence:

        Brain,



    activity:

        Activity



};









function MetricsCard({



    title="Metric",


    value="0",


    description="",


    type="activity"



}) {



    const Icon =

        ICON_MAP[type] ||

        Activity;








    return (





        <motion.div





            className="metrics-card"




            initial={{


                opacity:0,


                y:20



            }}



            animate={{


                opacity:1,


                y:0



            }}



            transition={{


                duration:0.4


            }}



            whileHover={{


                y:-5



            }}





        >







            <div className="metric-icon">





                <Icon size={24}/>





            </div>









            <div className="metric-content">





                <h3>


                    {title}


                </h3>









                <strong>


                    {value}


                </strong>









                {


                description &&



                (



                    <p>


                        {description}



                    </p>



                )



                }







            </div>









        </motion.div>






    );


}





export default MetricsCard;