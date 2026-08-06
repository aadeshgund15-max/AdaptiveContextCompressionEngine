/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Navbar Component

Responsible for:
- Application identity
- System status
- Navigation header
- Agent identity

=====================================================
*/


import {


    Activity,

    Brain,

    CircleUserRound,

    Wifi,

    Sparkles


} from "lucide-react";


import {


    motion


} from "framer-motion";









function Navbar(){



    return (





        <motion.nav





            className="navbar"





            initial={{


                opacity:0,


                y:-20



            }}



            animate={{


                opacity:1,


                y:0



            }}



            transition={{


                duration:0.5


            }}






        >







            {/* Brand */}



            <div className="navbar-brand">






                <div className="brand-icon">



                    <Brain size={28}/>



                </div>








                <div className="brand-text">



                    <h1>



                        ACIE



                    </h1>





                    <span>



                        Adaptive Context Intelligence Engine



                    </span>






                </div>







            </div>









            {/* System Status */}





            <div className="navbar-status">







                <div className="status-indicator">





                    <span className="online-dot"></span>





                    <span>



                        System Online



                    </span>






                </div>









                <div className="connection-status">





                    <Wifi size={18}/>





                    Backend Connected






                </div>







            </div>













            {/* Agent Identity */}





            <div className="navbar-user">







                <div className="agent-badge">





                    <Sparkles size={18}/>





                    AI Agent






                </div>









                <div className="user-info">





                    <span>



                        Mode



                    </span>





                    <strong>



                        Autonomous Intelligence



                    </strong>






                </div>









                <CircleUserRound size={32}/>






            </div>








        </motion.nav>





    );



}






export default Navbar;