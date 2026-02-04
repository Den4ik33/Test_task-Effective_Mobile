-- Задание 1: Абитуриенты
SELECT
    id,
    scores,
    RANK() OVER (ORDER BY scores DESC) AS position
FROM examination;


-- Задание 2: FULL JOIN
-- Ответ: Минимально 30 и максимально 50 строк.

-- Задание 3: Покупки
SELECT
    a.client_id
FROM account a
JOIN transaction t
    ON a.id = t.account_id
WHERE t.transaction_date >= CURRENT_DATE - INTERVAL '1 month'
GROUP BY a.client_id
HAVING SUM(t.amount) < 5000;
