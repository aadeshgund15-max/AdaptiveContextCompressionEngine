/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Chat Page

Responsible for:
- User interaction
- AI conversations
- Reasoning visualization

=====================================================
*/


import {


    useState


} from "react";


import {


    motion


} from "framer-motion";


import ChatBox from "../components/ChatBox";


import ReasoningTrace from "../components/ReasoningTrace";









function Chat(){





    const [trace,setTrace] = useState([]);









    return (







        <motion.div





            className="chat-page"





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



                    ACIE Chat



                </h1>








                <p>



                    Interact with Adaptive Context Intelligence Engine



                </p>







            </div>









            <div className="chat-layout">







                <motion.div





                    className="chat-section"





                    initial={{


                        opacity:0,


                        x:-20



                    }}



                    animate={{


                        opacity:1,


                        x:0



                    }}





                >






                    <ChatBox



                        onTraceUpdate={setTrace}



                    />







                </motion.div>













                <motion.div





                    className="reasoning-section"





                    initial={{


                        opacity:0,


                        x:20



                    }}



                    animate={{


                        opacity:1,


                        x:0



                    }}





                >







                    <ReasoningTrace





                        trace={trace}





                    />








                </motion.div>








            </div>








        </motion.div>







    );


}






export default Chat;