/*
=====================================================

Adaptive Context Intelligence Engine (ACIE)

useChat Hook

=====================================================
*/

import { useState } from "react";

import { sendChatMessage } from "../api/client";

function useChat() {

    const [messages, setMessages] = useState([]);

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState(null);

    const sendMessage = async (query) => {

        if (!query.trim()) return null;

        const userMessage = {
            role: "user",
            content: query
        };

        setMessages((prev) => [...prev, userMessage]);

        setLoading(true);

        setError(null);

        try {

            const response = await sendChatMessage(query);

            const aiMessage = {
                role: "assistant",
                content:
                    response.answer ||
                    response.response ||
                    "No response generated."
            };

            setMessages((prev) => [...prev, aiMessage]);

            return response;

        } catch (err) {

            console.error(err);

            setError(err.message);

            setMessages((prev) => [
                ...prev,
                {
                    role: "assistant",
                    content:
                        "Unable to connect with ACIE backend."
                }
            ]);

            return null;

        } finally {

            setLoading(false);

        }

    };

    const clearChat = () => {

        setMessages([]);

        setError(null);

    };

    return {

        messages,

        loading,

        error,

        sendMessage,

        clearChat

    };

}

export default useChat;