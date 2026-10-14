ef calculate_simple_interest(principal: float, rate: float, time: float) -> float:
  """Calculate simple interest using (P * R * T) / 100."""
  if principal < 0 or rate < 0 or time < 0:
    raise ValueError("Principal, rate, and time must be non-negative.")
  return (principal * rate * time) / 100