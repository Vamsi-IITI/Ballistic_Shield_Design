'''NOTE : All workflows will not be recorded, as recording is under development.'''

#region UI Action
with Transaction(True):
    body_20.Material = "0b11100b-3877-44f6-9845-9e3aee687bed"
#endregion


#region Details View Action
body_29.StiffnessBehavior = StiffnessBehavior.Rigid
#endregion

#region Context Menu Action
initial_conditions_46 = DataModel.GetObjectById(46)
initial_condition_56 = initial_conditions_46.InsertVelocity()
#endregion

#region Details View Action
selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selection.Ids = [6970]
initial_condition_56.Location = selection
#endregion

#region Details View Action
initial_condition_56.DefineBy = LoadDefineBy.Components
#endregion

#region Details View Action
initial_condition_56.XComponent = Quantity(-400000, "")
#endregion

#region Context Menu Action
solution_42 = DataModel.GetObjectById(42)
equivalent_plastic_strain_rst58 = solution_42.AddEquivalentPlasticStrainRST()
#endregion

#region Context Menu Action
equivalent_stress_59 = solution_42.AddEquivalentStress()
#endregion

#region Context Menu Action
total_deformation_60 = solution_42.AddTotalDeformation()
#endregion

#region Details View Action
selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selection.Ids = [6912]
total_deformation_60.Location = selection
#endregion

#region Context Menu Action
velocity_probe_62 = solution_42.AddVelocityProbe()
#endregion

#region Details View Action
selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selection.Ids = [6970]
velocity_probe_62.GeometryLocation = selection
#endregion

#region Details View Action
velocity_probe_62.ResultSelection = ProbeDisplayFilter.XAxis
#endregion

#region Context Menu Action
analysis_41 = DataModel.GetObjectById(41)
fixed_support_65 = analysis_41.AddFixedSupport()
#endregion

#region Details View Action
selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selection.Ids = [6907, 6908, 6909, 6906]
fixed_support_65.Location = selection
#endregion

#region Context Menu Action
fixed_support_67 = analysis_41.AddFixedSupport()
#endregion

#region Details View Action
selection = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.GeometryEntities)
selection.Ids = [33, 30, 31, 32]
fixed_support_67.Location = selection
#endregion

#region Details View Action
mesh_15 = Model.Mesh
mesh_15.ElementSize = Quantity(1, "mm")
#endregion
