/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

Memory Panel Component

Responsible for:
- Displaying agent memories
- Showing memory metadata
- Memory intelligence visualization

Logic handled by:
- useMemory Hook

=====================================================
*/


import {

    Brain,

    Database,

    Target,

    Activity,

    RefreshCw

} from "lucide-react";


import useMemory from "../hooks/useMemory";







function MemoryPanel(){





    const {


        memories,


        loading,


        error,


        refresh



    } = useMemory();









    return (




        <div className="memory-panel">





            <div className="panel-header">





                <Brain size={22}/>




                <h2>

                    ACIE Memory

                </h2>







                <button


                    className="refresh-btn"


                    onClick={refresh}



                >



                    <RefreshCw size={16}/>



                </button>





            </div>









            {

            loading &&



            (

                <p>

                    Loading memories...

                </p>

            )

            }









            {

            error &&



            (

                <p className="error-text">


                    Memory service unavailable.


                </p>


            )

            }









            {


            !loading &&

            memories.length===0 &&



            (

                <p>

                    No memories available.

                </p>

            )

            }









            <div className="memory-list">







                {


                memories.map(



                    (memory,index)=>(





                        <div



                        key={

                            memory.id ||

                            index

                        }



                        className="memory-item"



                        >








                            <div className="memory-title">





                                <Database size={18}/>





                                <h3>

                                    {


                                    memory.title ||

                                    memory.query ||

                                    "Memory"



                                    }


                                </h3>




                            </div>









                            <p>

                                {


                                memory.content ||

                                memory.text ||

                                "Stored context"



                                }


                            </p>









                            <div className="memory-meta">







                                <span>



                                    <Target size={14}/>




                                    Importance:


                                    {" "}


                                    {


                                    memory.importance ||

                                    0



                                    }




                                </span>









                                <span>



                                    <Activity size={14}/>




                                    Confidence:


                                    {" "}



                                    {


                                    memory.confidence ||

                                    0



                                    }




                                </span>






                            </div>









                        </div>





                    )


                )


                }









            </div>








        </div>





    );





}




export default MemoryPanel;