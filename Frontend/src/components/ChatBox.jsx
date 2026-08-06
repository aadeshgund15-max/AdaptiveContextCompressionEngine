/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

ChatBox Component

=====================================================
*/

import { useState } from "react";

import {
    Send,
    User,
    Bot,
    Loader2
} from "lucide-react";

import useChat from "../hooks/useChat";

function ChatBox({ onTraceUpdate }) {

    const [message, setMessage] = useState("");

    const {
        messages,
        loading,
        sendMessage
    } = useChat();

    const handleSend = async () => {

        if (!message.trim() || loading) return;

        const query = message.trim();

        setMessage("");

        try {

            const response = await sendMessage(query);

            if (response?.execution) {
                onTraceUpdate?.(response.execution);
            }

        } catch (error) {

            console.error("Chat Error:", error);

        }

    };

    const handleKeyDown = (event) => {

        if (event.key === "Enter" && !event.shiftKey) {

            event.preventDefault();

            handleSend();

        }

    };

    return (

        <div className="chat-box">

            <div className="chat-messages">

                {messages.length === 0 && (

                    <div className="empty-chat">

                        <Bot size={40} />

                        <h2>Ask ACIE Anything</h2>

                        <p>
                            Adaptive Context Intelligence Engine
                        </p>

                    </div>

                )}

                {messages.map((msg, index) => (

                    <div
                        key={index}
                        className={
                            msg.role === "user"
                                ? "message user"
                                : "message assistant"
                        }
                    >

                        {msg.role === "user"
                            ? <User size={18} />
                            : <Bot size={18} />
                        }

                        <div className="message-content">

                            <p>{msg.content}</p>

                        </div>

                    </div>

                ))}

                {loading && (

                    <div className="message assistant">

                        <Loader2
                            className="spin"
                            size={18}
                        />

                        <p>ACIE is thinking...</p>

                    </div>

                )}

            </div>

            <div className="chat-input">

                <input
                    type="text"
                    placeholder="Ask ACIE anything..."
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    onKeyDown={handleKeyDown}
                    disabled={loading}
                />

                <button
                    onClick={handleSend}
                    disabled={loading || !message.trim()}
                >

                    <Send size={18} />

                </button>

            </div>

        </div>

    );

}

export default ChatBox;