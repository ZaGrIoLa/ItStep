import warnings

warnings.simplefilter("ignore",SyntaxWarning)
warnings.simplefilter("error",ImportWarning)

warnings.warn("Warnind, no code here", SyntaxWarning)
try:

  warnings.warn("Warning? module no import", ImportWarning)

except:
    print("Warning processe")