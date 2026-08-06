/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Sidebar Component

Responsible for:
- Application navigation
- Route switching
- ACIE modules access

=====================================================
*/


import {


    LayoutDashboard,

    MessageSquare,

    Database,

    BarChart3,

    Settings,

    BrainCircuit,

    X,

    Sparkles


} from "lucide-react";



import {


    NavLink


} from "react-router-dom";



import {


    motion


} from "framer-motion";









function Sidebar({


    open=true,


    closeSidebar



}) {






    const menuItems=[




        {


            name:"Dashboard",


            path:"/",


            icon:LayoutDashboard



        },





        {


            name:"Chat",


            path:"/chat",


            icon:MessageSquare



        },






        {


            name:"Memory",


            path:"/memory",


            icon:Database



        },






        {


            name:"Evaluation",


            path:"/evaluation",


            icon:BarChart3



        },






        {


            name:"Agent Settings",


            path:"/settings",


            icon:Settings



        }





    ];











    return (






        <motion.aside





            className={

                open

                ?

                "sidebar open"

                :

                "sidebar"

            }






            initial={{


                x:-80,


                opacity:0



            }}



            animate={{


                x:0,


                opacity:1



            }}



            transition={{


                duration:0.4


            }}





        >







            {/* Header */}





            <div className="sidebar-header">






                <div className="sidebar-logo">






                    <div className="logo-circle">



                        <BrainCircuit size={28}/>



                    </div>







                    <div>



                        <h2>



                            ACIE



                        </h2>





                        <span>



                            Agent Console



                        </span>






                    </div>







                </div>










                {


                closeSidebar &&




                (

                    <button



                    onClick={closeSidebar}



                    className="close-button"



                    >




                        <X size={20}/>




                    </button>


                )



                }





            </div>












            {/* AI Badge */}





            <div className="sidebar-ai-badge">





                <Sparkles size={16}/>



                Autonomous Intelligence





            </div>













            {/* Navigation */}






            <nav className="sidebar-menu">







                {

                menuItems.map((item,index)=>{





                    const Icon=item.icon;





                    return (







                    <NavLink





                    key={index}





                    to={item.path}





                    className={({isActive})=>



                        isActive

                        ?

                        "active"

                        :

                        ""



                    }





                    >








                        <motion.div



                            whileHover={{

                                scale:1.1

                            }}



                        >



                            <Icon size={20}/>



                        </motion.div>









                        <span>



                            {item.name}



                        </span>







                    </NavLink>







                    )



                })



                }






            </nav>












            {/* Footer */}






            <div className="sidebar-footer">







                <span>



                    ACIE Core



                </span>







                <strong>



                    Version 1.0.0



                </strong>







            </div>









        </motion.aside>






    );





}







export default Sidebar;