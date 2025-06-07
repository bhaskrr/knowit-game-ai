"use client";
import { useParams } from "next/navigation";
import { useState, useEffect } from "react";

type Option = { id: number; text: string; is_correct: boolean };
type Question = { id: number; text: string; options: Option[] };

export default function Trivia() {
  const { id } = useParams();
  const [questions, setQuestions] = useState<Question[]>([]);
  const [answers, setAnswers] = useState<{
    [questionId: number]: number | null;
  }>({});
  const [showResult, setShowResult] = useState<{
    [questionId: number]: boolean;
  }>({});
  const [current, setCurrent] = useState(0);
  const [finished, setFinished] = useState(false);

  useEffect(() => {
    const fetchAndSetQuestions = async () => {
      try {
        const questionsUrl =
          process.env.NEXT_PUBLIC_GET_TOPICS_URL + `/${id}/trivia`;
        if (!questionsUrl) {
          throw new Error(
            "NEXT_PUBLIC_GET_TOPICS_URL environment variable is not set"
          );
        }
        const response = await fetch(questionsUrl, { method: "GET" });
        const data = await response.json();
        if (data !== undefined) {
          setQuestions(data);
        } else {
          console.warn("Data is null");
        }
      } catch (error) {
        console.error("Failed to fetch questions:", error);
      }
    };

    fetchAndSetQuestions();
  }, [id]);

  const handleSelect = (questionId: number, optionId: number) => {
    setAnswers((prev) => ({ ...prev, [questionId]: optionId }));
    setShowResult((prev) => ({ ...prev, [questionId]: true }));
  };

  const handleNext = () => {
    if (current < questions.length - 1) {
      setCurrent((prev) => prev + 1);
    } else {
      setFinished(true);
    }
  };

  if (!questions || questions.length === 0) {
    return (
      <div className="text-center text-lg text-gray-500 py-10">Loading...</div>
    );
  }

  if (finished) {
    // You can customize this section to show a summary or score
    return (
      <div className="flex flex-col items-center justify-center min-h-screen">
        <div className="bg-white rounded-2xl shadow-xl p-8 border border-purple-100 text-center">
          <h2 className="text-2xl font-bold text-purple-700 mb-4">
            Quiz Complete!
          </h2>
          <p className="text-lg text-gray-700 mb-2">
            You answered {Object.keys(answers).length} out of {questions.length}{" "}
            questions.
          </p>
          <p className="text-md text-green-600 font-semibold">
            Score:{" "}
            {
              questions.filter((q) => {
                const userAnswer = answers[q.id];
                const correctOption = q.options.find((opt) => opt.is_correct);
                return userAnswer === correctOption?.id;
              }).length
            }{" "}
            / {questions.length}
          </p>
        </div>
      </div>
    );
  }

  const q = questions[current];
  const show = showResult[q.id];

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-blue-50 to-amber-50 py-10 px-2 flex flex-col items-center justify-center">
      <div className="max-w-xl w-full mx-auto space-y-8">
        <div className="bg-white rounded-2xl shadow-xl p-6 border border-purple-100 hover:shadow-2xl transition-all duration-300">
          <div className="flex justify-between items-center mb-2">
            <span className="text-xs text-gray-400">
              Question {current + 1} of {questions.length}
            </span>
          </div>
          <h3 className="text-xl font-bold text-purple-800 mb-4">{q.text}</h3>
          <div className="space-y-3">
            {q.options.map((opt) => {
              const isSelected = answers[q.id] === opt.id;
              const isCorrect = opt.is_correct;
              return (
                <label
                  key={opt.id}
                  htmlFor={`q${q.id}_opt${opt.id}`}
                  className={`flex items-center gap-3 px-4 py-2 rounded-lg cursor-pointer border transition
                    ${
                      isSelected
                        ? isCorrect
                          ? "bg-green-100 border-green-400"
                          : "bg-red-100 border-red-400"
                        : "bg-gray-50 border-gray-200 hover:bg-purple-50"
                    }
                    ${show && isCorrect ? "ring-2 ring-green-400" : ""}
                  `}
                >
                  <input
                    type="radio"
                    name={`question_${q.id}`}
                    id={`q${q.id}_opt${opt.id}`}
                    checked={isSelected}
                    disabled={show}
                    onChange={() => handleSelect(q.id, opt.id)}
                    className="accent-purple-600"
                  />
                  <span className="text-base font-medium">{opt.text}</span>
                  {show && isSelected && (
                    <span
                      className={`ml-2 text-sm font-bold ${
                        isCorrect ? "text-green-600" : "text-red-600"
                      }`}
                    >
                      {isCorrect ? "Correct!" : "Wrong"}
                    </span>
                  )}
                  {show && !isSelected && isCorrect && (
                    <span className="ml-2 text-xs text-green-500 font-semibold">
                      (Correct Answer)
                    </span>
                  )}
                </label>
              );
            })}
          </div>
          <div className="flex justify-end mt-6">
            <button
              className={`px-6 py-2 rounded-lg font-bold text-white bg-gradient-to-r from-purple-500 to-blue-500 shadow-lg hover:from-purple-600 hover:to-blue-600 transition disabled:opacity-50`}
              disabled={!show}
              onClick={handleNext}
            >
              {current === questions.length - 1 ? "Finish" : "Next"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
