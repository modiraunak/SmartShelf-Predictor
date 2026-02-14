"""import the necessary libraries"""
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import pytesseract
import re
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from utils.image_processor import ImageProcessor
from utils.ocr_extractor import OCRExtractor
from utils.health_scorer import HealthScorer
from utils.demand_predictor import DemandPredictor