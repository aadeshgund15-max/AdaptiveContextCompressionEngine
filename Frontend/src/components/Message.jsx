/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Message Component

Responsible for:
- Rendering chat messages
- User/AI separation
- Message presentation
- Message animations

=====================================================
*/


import {

    User,

    Bot

} from "lucide-react";


import {

    motion

} from "framer-motion";







function Message({


    role,

    content,

    timestamp



}) {



    const isUser = role === "user";






    return (



        <motion.div



            className={


                isUser

                ?

                "message user"

                :

                "message assistant"


            }




            initial={{


                opacity:0,


                y:10



            }}



            animate={{


                opacity:1,


                y:0



            }}



            transition={{


                duration:0.3


            }}



        >






            <div className="message-icon">





                {


                isUser

                ?


                <User size={18}/>


                :


                <Bot size={18}/>



                }





            </div>









            <div className="message-content">





                <p>


                    {


                    content ||

                    "No message content"



                    }


                </p>









                {


                timestamp &&



                (



                    <span className="message-time">


                        {


                        new Date(timestamp)

                        .toLocaleTimeString()



                        }


                    </span>



                )



                }





            </div>







        </motion.div>





    );


}





export default Message;