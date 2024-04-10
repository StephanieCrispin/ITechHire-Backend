from pydantic import BaseModel
from typing import Optional,List
from enum import Enum

class TechSpecialization(str,Enum):
    ArtificialIntelligence = "artificialIntelligence"
    MachineLearning = "machineLearning"
    DataScience = "dataScience"
    Cybersecurity = "cybersecurity"
    CloudComputing = "cloudComputing"
    DevOps = "devOps"
    Blockchain = "blockchain"
    InternetOfThings = "internetOfThings"
    BigData = "bigData"
    AugmentedReality = "augmentedReality"
    VirtualReality = "virtualReality"
    FullStackDevelopment = "fullStackDevelopment"
    MobileAppDevelopment = "mobileAppDevelopment"
    WebDevelopment = "webDevelopment"
    SoftwareEngineering = "softwareEngineering"
    UIUXDesign = "uiUxDesign"
    GameDevelopment = "gameDevelopment"
    EmbeddedSystems = "embeddedSystems"
    Robotics = "robotics"
    QuantumComputing = "quantumComputing"




class Technologies(str,Enum):
    Python = "python"
    JavaScript = "javaScript"
    Java = "java"
    ReactJs = "reactJs"
    Angular = "angular"
    NodeJs = "nodeJs"
    Ruby = "ruby"
    Flask = "flask"
    SpringBoot = "springBoot"
    Django = "django"
    VueJs = "vueJs"
    TypeScript = "typeScript"
    Swift = "swift"
    Kotlin = "kotlin"
    DotNetCore = ".netCore"
    RubyOnRails = "rubyOnRails"
    ExpressJs = "expressJs"
    TensorFlow = "tensorFlow"
    Pandas = "pandas"
    JQuery = "jquery"
    Bootstrap = "bootstrap"
    Laravel = "laravel"
    Docker = "docker"
    Kubernetes = "kubernetes"
    PyTorch = "pyTorch"
    Git = "git"
    Jenkins = "jenkins"

class UpdateMentor(BaseModel):
    specialization: Optional[TechSpecialization] = None
    about:Optional[str] = None
    technologies : Optional[List[Technologies]] = None
    facebookURL: Optional[str] = None
    twitterURL: Optional[str] = None
    youtubeURL: Optional[str] = None